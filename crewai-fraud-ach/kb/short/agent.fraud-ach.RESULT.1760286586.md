```json
{
  "id": "c36dae7c3b3c56a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286586,
  "host_pid": "9e6742732c60:1",
  "hash": "04ab0fff0b19ec2c90c3119456c76ae827cce861ed5219344c1172c765fd27e3",
  "cid": "QmV104ab0fff0b19ec2c90c3119456c76ae827cce861",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286586,
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
      "evaluated_at": 1760286586
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
  "sig": "c020dbe8c1feff0c54cf7711305822d74837c546739c096b9d90969e56d18b46"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026081546
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285763, 'matching_hash': 'ce75c9757255dcb1'}}}