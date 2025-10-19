```json
{
  "id": "c6c195f60fbf6cc5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289340,
  "host_pid": "9e6742732c60:1",
  "hash": "c57b07ced24e908eaf984ea45e7805484178a044434661a663836ce71020acb2",
  "cid": "QmV1c57b07ced24e908eaf984ea45e7805484178a044",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289340,
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
      "evaluated_at": 1760289340
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
  "sig": "858fe6122aef9a9ca4085daa3dcefe850ce9109ae7e83e27924e87b3faad6570"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 589241761167275
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 37633680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285765, 'matching_hash': 'a1dced1ef969015f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '589241760', 'validation_error': 'Invalid routing number checksum'}}}