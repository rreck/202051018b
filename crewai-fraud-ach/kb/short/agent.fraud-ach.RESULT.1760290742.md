```json
{
  "id": "027065786806b620",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290742,
  "host_pid": "9e6742732c60:1",
  "hash": "23334d1f1a787feb904268968d251311641cc6cb318f6729c66f7453c7a242a7",
  "cid": "QmV123334d1f1a787feb904268968d251311641cc6cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290742,
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
      "evaluated_at": 1760290743
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
  "sig": "cf1ddf825669ee13252d36918ddffe652faf34cfae04126cdf411bd52b42ebfb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157192911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 42413362, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285764, 'matching_hash': 'e4f1eedb707bab1f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '208726934', 'validation_error': 'Invalid routing number checksum'}}}