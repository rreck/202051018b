```json
{
  "id": "f9fab7ff7359964e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289127,
  "host_pid": "9e6742732c60:1",
  "hash": "5ff51909dbdb4db9a83e13913739622c99e012e4c8c5e1744f2fc413a276ac33",
  "cid": "QmV15ff51909dbdb4db9a83e13913739622c99e012e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289127,
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
      "evaluated_at": 1760289127
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
  "sig": "4f20d3955700f328b01c0d930047bea415c0dd073ff58122d97d359d39c77bb1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027229959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 49511910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': 'f31e697a4f515fbb'}}}