```json
{
  "id": "c53fdbdfaeffc13f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288172,
  "host_pid": "9e6742732c60:1",
  "hash": "27b0a5b15225572dba510bec6b4199c9cb79f24bddbb0a47032899b7a0a8a965",
  "cid": "QmV127b0a5b15225572dba510bec6b4199c9cb79f24b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288172,
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
      "evaluated_at": 1760288172
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
  "sig": "48d46d79c2ac0c0e3afbb6c04f30fb527affd347a3511c2dad2f13f7ab94fe61"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598152937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 21250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': '12ca21f72ace6b8c'}}}