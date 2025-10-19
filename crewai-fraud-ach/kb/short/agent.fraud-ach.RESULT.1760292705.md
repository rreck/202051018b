```json
{
  "id": "c9d57c0f548e7043",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292705,
  "host_pid": "9e6742732c60:1",
  "hash": "10d5214db373de754e120ccf339e3ac1d654dc1cbe89a5135527670556853bd7",
  "cid": "QmV110d5214db373de754e120ccf339e3ac1d654dc1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292705,
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
      "evaluated_at": 1760292705
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
  "sig": "1f5c321314c26d681608a042fe10f2d22f656a0eb7b944d934d09cd255ec4604"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 039274533993332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 33081489, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285765, 'matching_hash': 'a2ad50f9b8d4dabc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '039274537', 'validation_error': 'Invalid routing number checksum'}}}