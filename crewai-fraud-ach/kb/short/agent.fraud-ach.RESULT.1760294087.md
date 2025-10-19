```json
{
  "id": "dc6572c43078d020",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294087,
  "host_pid": "9e6742732c60:1",
  "hash": "45bad53048ab433f01aca91a3ffeaf38852aec967adb22f5a4a08cbf1b6538b5",
  "cid": "QmV145bad53048ab433f01aca91a3ffeaf38852aec96",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294087,
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
      "evaluated_at": 1760294087
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
  "sig": "3b78e24279db79d932dd8b1e7e5ade1c3a8e4f63a37dc568e0d2ed3e3869d1bd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 288759219871928
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 98719929, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '2df17da091128ee2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '288759214', 'validation_error': 'Invalid routing number checksum'}}}