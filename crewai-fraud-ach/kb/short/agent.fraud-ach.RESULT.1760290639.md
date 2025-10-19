```json
{
  "id": "c5828294217db2e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290639,
  "host_pid": "9e6742732c60:1",
  "hash": "ea5cd6a616fb8ef48219413ed9b785d048cc2b390e48a40cad903e5b0969cd4f",
  "cid": "QmV1ea5cd6a616fb8ef48219413ed9b785d048cc2b39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290639,
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
      "evaluated_at": 1760290639
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
  "sig": "e22725693e46793b723a8f0e0a4b3b31e585dc77a0ceeae5f48e0839e4b4de03"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 699349871536240
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 57927375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285765, 'matching_hash': '372ab63252fc0966'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '699349873', 'validation_error': 'Invalid routing number checksum'}}}