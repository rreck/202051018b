```json
{
  "id": "15ca2ad5249e84e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292056,
  "host_pid": "9e6742732c60:1",
  "hash": "a9e77351dfa6d583a3f20cafc42ca5cb71d035d8f30c1ef73189b67d1f057012",
  "cid": "QmV1a9e77351dfa6d583a3f20cafc42ca5cb71d035d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292056,
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
      "evaluated_at": 1760292056
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
  "sig": "f917b26e8abdafce9fe0147cb4dd9dd14b45cc4fcbc2b5f602139f00198b26dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591685004
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 62154918, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': 'e63d914157ffc7ed'}}}