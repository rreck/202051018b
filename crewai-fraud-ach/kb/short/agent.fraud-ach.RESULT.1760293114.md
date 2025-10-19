```json
{
  "id": "04212cb5260434f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293114,
  "host_pid": "9e6742732c60:1",
  "hash": "cb42b3adfc989d97b2a007203bc762975ff11d33ddb731bf9132d58bef2e2b38",
  "cid": "QmV1cb42b3adfc989d97b2a007203bc762975ff11d33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293114,
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
      "evaluated_at": 1760293114
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
  "sig": "32d4328a94314631e3c06f9199dd232429933a319c2360dab0203fb7da41613f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038823890
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 44295492, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '81df70e06ca09887'}}}