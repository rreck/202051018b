```json
{
  "id": "63354acd51de2e8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292932,
  "host_pid": "9e6742732c60:1",
  "hash": "a59dfe93734c52c488f968a508c8adbf028f01cb74460bca0a3ed4b596359345",
  "cid": "QmV1a59dfe93734c52c488f968a508c8adbf028f01cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292932,
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
      "evaluated_at": 1760292932
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
  "sig": "27717dfc2695d0ab1fb2a02fb7983d8b22cc3f1da48c2b500485976ea5e7bbf8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028384993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 76018384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285764, 'matching_hash': '07aae5a269425bd8'}}}