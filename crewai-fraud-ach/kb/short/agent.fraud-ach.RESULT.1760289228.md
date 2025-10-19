```json
{
  "id": "baff9db6fb86a95e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289228,
  "host_pid": "9e6742732c60:1",
  "hash": "b99120370407b61c485dc1b491f2ae2bbbf3c2e8e734df75ffd3dc184eaa2357",
  "cid": "QmV1b99120370407b61c485dc1b491f2ae2bbbf3c2e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289228,
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
      "evaluated_at": 1760289228
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
  "sig": "62f470eef607897f33eb73719701adecf4864635be0404b435a4947eca89b1c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596690593
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 27204315, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760284979, 'matching_hash': 'a761076f0402b0d4'}}}