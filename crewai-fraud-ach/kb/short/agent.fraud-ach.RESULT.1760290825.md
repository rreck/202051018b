```json
{
  "id": "6d433b8875c3633e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290825,
  "host_pid": "9e6742732c60:1",
  "hash": "df8304902100fde1ad49a51fded1e215ae3f7521c74ffa6d4d59cd303a2fb8d6",
  "cid": "QmV1df8304902100fde1ad49a51fded1e215ae3f7521",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290825,
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
      "evaluated_at": 1760290825
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
  "sig": "211f6a7eec7b9e3655d83758ea4185c9b32071657249e41366c68356f1e55aaa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157869633
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 20355840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': '3a805d178d839f31'}}}