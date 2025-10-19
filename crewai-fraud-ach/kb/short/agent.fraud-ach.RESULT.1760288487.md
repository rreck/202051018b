```json
{
  "id": "a28628022c2d846b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288487,
  "host_pid": "9e6742732c60:1",
  "hash": "83bada025cf7ea2349a7e297f4246edaec34f75866b1ab3176a2670506561af4",
  "cid": "QmV183bada025cf7ea2349a7e297f4246edaec34f758",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288487,
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
      "evaluated_at": 1760288488
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
  "sig": "048af14b3a7aed81f3062e4938db6f302bfba74b074b7205bec182d8c8d49b58"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 530764332360017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 19443270, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285763, 'matching_hash': '09bd6f4aa98253cc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '530764331', 'validation_error': 'Invalid routing number checksum'}}}