```json
{
  "id": "b6045abbc0bde9f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294815,
  "host_pid": "9e6742732c60:1",
  "hash": "3d256ccee4a5215d31926669587ad50063e2b3b159b2ef2a38fe461e8a5080de",
  "cid": "QmV13d256ccee4a5215d31926669587ad50063e2b3b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294815,
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
      "evaluated_at": 1760294815
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
  "sig": "5b3f36f91b13570f0ee1476967394700558c0562dd1fad74c5594c52f49ecea9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466524554
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 93695840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'c9a1c21cbf3363ae'}}}