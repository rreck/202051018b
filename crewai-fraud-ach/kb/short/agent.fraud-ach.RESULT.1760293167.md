```json
{
  "id": "47534e1443c467f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293167,
  "host_pid": "9e6742732c60:1",
  "hash": "f52f6de0dc6245387e50853c8018255bbc3f6443320116f691e9bf6c3f3b0c83",
  "cid": "QmV1f52f6de0dc6245387e50853c8018255bbc3f6443",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293167,
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
      "evaluated_at": 1760293167
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
  "sig": "5abb5fcbf6429d37d84af9ea7215662e8fe90d0f782c68cb212b5e36600dd5b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020120978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 20533626, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '55bccccaf90262bb'}}}