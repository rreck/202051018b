```json
{
  "id": "55df3c0183d994dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294885,
  "host_pid": "9e6742732c60:1",
  "hash": "aab3d4452aaa9c55f343c64ccadb8dd62ac20f40d2b52132ca45365dca229a26",
  "cid": "QmV1aab3d4452aaa9c55f343c64ccadb8dd62ac20f40",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294885,
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
      "evaluated_at": 1760294885
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
  "sig": "fe2a061b65578f5b6fe0baa7b52b79050d0df514aa472bbe3c2a9160bba4eeaa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272135261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 322, 'threshold': 50, 'total_amount': 102828768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 321, 'first_seen': 1760284979, 'matching_hash': 'c71937e0bf846771'}}}