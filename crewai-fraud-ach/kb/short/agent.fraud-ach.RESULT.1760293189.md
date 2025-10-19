```json
{
  "id": "fc73b05a141c5b71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293189,
  "host_pid": "9e6742732c60:1",
  "hash": "e5384f7633d301f4f959d9d35ca8619140261e98cdaa63492ff1b5e92e407b0b",
  "cid": "QmV1e5384f7633d301f4f959d9d35ca8619140261e98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293189,
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
      "evaluated_at": 1760293189
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
  "sig": "cd1704ad0e6af429e26443e14c6e0aefca619aaac42c21d49e8bb30e1c4d74cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156494107
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 106303401, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285764, 'matching_hash': 'c1327b457e76afdd'}}}