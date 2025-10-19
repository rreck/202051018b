```json
{
  "id": "723f56578cb1ae5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294363,
  "host_pid": "9e6742732c60:1",
  "hash": "a62fa6389c9c520ee04123f400b304ddd84cb4b3084843a410affeb54ec47b20",
  "cid": "QmV1a62fa6389c9c520ee04123f400b304ddd84cb4b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294363,
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
      "evaluated_at": 1760294363
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
  "sig": "9f966ccbed25bc65c210bc19f579dbb69306741690f4f68ebd0826dc98d0eded"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 75106528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}