```json
{
  "id": "84cd1e978fa4f51c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290827,
  "host_pid": "9e6742732c60:1",
  "hash": "49398094419a89847befe032298db6f24c4ce9268d23a184c69a3676666752b0",
  "cid": "QmV149398094419a89847befe032298db6f24c4ce926",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290827,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760290827
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "0bdab4d02a8fff06f37cb22ace5ee1d89dcf2e23878eb21816baf9dcc0c5ee4a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243386632
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 35488800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': 'a6aa6f7765b452ca'}}}