```json
{
  "id": "fb91b6eaf8fbcf3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286780,
  "host_pid": "9e6742732c60:1",
  "hash": "9e9ab6ec9c4ec85692fc19c89e903f7c92047984e9b52f8d84362ed8788c4a85",
  "cid": "QmV19e9ab6ec9c4ec85692fc19c89e903f7c92047984",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286780,
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
      "evaluated_at": 1760286780
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
  "sig": "7c1191aa6abbe387093107af7c0098ffc658f5fc100e76d0e9e773526c783818"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 085520768954692
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17967903, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285763, 'matching_hash': '4f8cdcee5609bbf1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}