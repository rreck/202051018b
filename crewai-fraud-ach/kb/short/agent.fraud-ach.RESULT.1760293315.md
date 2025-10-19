```json
{
  "id": "d37fa3ab0b8a7978",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293315,
  "host_pid": "9e6742732c60:1",
  "hash": "726a3406a0fc333a5ef6051cd470e7e53ea8a8f86ea14421a4367d8ce2d96440",
  "cid": "QmV1726a3406a0fc333a5ef6051cd470e7e53ea8a8f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293315,
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
      "evaluated_at": 1760293315
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
  "sig": "eca878662008243277b9a5942d426b2985f2ed1857a77eeb908e8500e945fbef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244248906
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 30229848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285764, 'matching_hash': '29854d353b99a4c0'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}