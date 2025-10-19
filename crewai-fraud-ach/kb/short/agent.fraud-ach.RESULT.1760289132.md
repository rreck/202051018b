```json
{
  "id": "f9a0a60dd6c0666f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289132,
  "host_pid": "9e6742732c60:1",
  "hash": "517ea0d6261d8e6ffda8555ff1f4af4ceabe438a0e860461b66cd5e3efdb84e7",
  "cid": "QmV1517ea0d6261d8e6ffda8555ff1f4af4ceabe438a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289132,
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
      "evaluated_at": 1760289132
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
  "sig": "6d8539fb55398cf20816f6ca25a3e328ec27dae064da0af33cd50831f6553b36"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 130120308000996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 27956676, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285765, 'matching_hash': 'd5206edc25c84cce'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '130120307', 'validation_error': 'Invalid routing number checksum'}}}