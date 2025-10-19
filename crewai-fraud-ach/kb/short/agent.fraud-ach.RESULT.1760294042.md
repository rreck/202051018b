```json
{
  "id": "251e48581a351985",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294042,
  "host_pid": "9e6742732c60:1",
  "hash": "1f132c93210094cbd9d8129b0e6e8a4314a2d8ff55981637528c58277550d9a9",
  "cid": "QmV11f132c93210094cbd9d8129b0e6e8a4314a2d8ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294042,
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
      "evaluated_at": 1760294042
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
  "sig": "543361af3738c005a6a95aaf2db495c99b536f874a4f8e29214f81dfaaf064aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590909791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 21803770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285765, 'matching_hash': 'dd7dbd0f0c1d6f0c'}}}