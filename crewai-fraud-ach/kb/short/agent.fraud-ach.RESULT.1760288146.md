```json
{
  "id": "7c95ac6dc854c665",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288146,
  "host_pid": "9e6742732c60:1",
  "hash": "4421ef7f49d4551bbd21cf6c39339cb8add535abbc0a991db72ac4691ab719dc",
  "cid": "QmV14421ef7f49d4551bbd21cf6c39339cb8add535ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288146,
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
      "evaluated_at": 1760288146
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
  "sig": "6f2bb0dead079c6d427c4a9d1417ed03228749f82508473884f0d79b26b9e00b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 30302496, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}