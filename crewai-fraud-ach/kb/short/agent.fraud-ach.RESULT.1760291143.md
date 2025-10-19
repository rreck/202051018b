```json
{
  "id": "dd3573822fd55a61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291143,
  "host_pid": "9e6742732c60:1",
  "hash": "036c30ef43502805184e0fb64223906fcbd23e6638716e809665bf9afe8e6034",
  "cid": "QmV1036c30ef43502805184e0fb64223906fcbd23e66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291143,
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
      "evaluated_at": 1760291143
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
  "sig": "4a303443cf097c22d5888aa3b49249b9f9429a45098e9d2128a60fa53d61aabf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027669266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 13962984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285764, 'matching_hash': 'fbd07eed8562f9d2'}}}