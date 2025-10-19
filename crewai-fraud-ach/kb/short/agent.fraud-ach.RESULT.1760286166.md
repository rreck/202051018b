```json
{
  "id": "f103e3e8783536ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286166,
  "host_pid": "9e6742732c60:1",
  "hash": "3cecb622767719f1a8d6bd285206026dae53ca7612f51458d9b115e7ea2e208c",
  "cid": "QmV13cecb622767719f1a8d6bd285206026dae53ca76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286166,
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
      "evaluated_at": 1760286166
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
  "sig": "896631b76bbf8f01163ec375aad5fb4d5db51cf9fdca7d6c0eead78e4d55be4d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}