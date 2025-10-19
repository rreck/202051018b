```json
{
  "id": "7c9b7b713362cf7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287913,
  "host_pid": "9e6742732c60:1",
  "hash": "8ac89bd53a3a6eceb711ea601fc81faa83954fdb85ae9273109a58e7f29f4669",
  "cid": "QmV18ac89bd53a3a6eceb711ea601fc81faa83954fdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287913,
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
      "evaluated_at": 1760287913
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "8b47f93ef75607aa7df6ad0528c980fba46d07bcf94e383fb957b066c862dc64"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 699349871536240
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 28403100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285765, 'matching_hash': '372ab63252fc0966'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '699349873', 'validation_error': 'Invalid routing number checksum'}}}