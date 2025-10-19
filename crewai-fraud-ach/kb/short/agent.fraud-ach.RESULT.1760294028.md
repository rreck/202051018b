```json
{
  "id": "c5226952d942cda8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294028,
  "host_pid": "9e6742732c60:1",
  "hash": "3e38018c005cb2000a5814a2d23e7c41f8da609921e26cb8ef1fae25f61e9476",
  "cid": "QmV13e38018c005cb2000a5814a2d23e7c41f8da6099",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294028,
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
      "evaluated_at": 1760294028
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
  "sig": "8290c5f86487cde8ca4a5e36ea4fabc5c121873314a1502ffd24581432fb1e60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599719457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 42746650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '97e4873137c26cd1'}}}