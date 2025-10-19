```json
{
  "id": "b5781fa76139e7d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286555,
  "host_pid": "9e6742732c60:1",
  "hash": "58d80c8edea75dc4a4ed0611a2105a97b844a99c581d1d8a76333238eeba6bcf",
  "cid": "QmV158d80c8edea75dc4a4ed0611a2105a97b844a99c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286555,
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
      "evaluated_at": 1760286555
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
  "sig": "50cea7d8d46a13ebba77444d58bf0e48f8eff49dffa497f46442ff81ba631a40"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026132147
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285765, 'matching_hash': 'fe0c58008e192989'}}}