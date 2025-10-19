```json
{
  "id": "761d3ee453af313d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292641,
  "host_pid": "9e6742732c60:1",
  "hash": "b34eef0ccf97d1ef884eb9569988653753301552819a79f31c197f7f25624eac",
  "cid": "QmV1b34eef0ccf97d1ef884eb9569988653753301552",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292641,
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
      "evaluated_at": 1760292641
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
  "sig": "102bdc95ff00e3bbf65ce38c305dfe243289d9e3f4307351e29b38305144de6e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026865262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 98927682, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': 'acc989ae5f5d7052'}}}