```json
{
  "id": "39b2c0f37c75b565",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294869,
  "host_pid": "9e6742732c60:1",
  "hash": "fbc40641e7b775d6a025a4c6416151ef6f2b98652e38b92316fc270578606ff3",
  "cid": "QmV1fbc40641e7b775d6a025a4c6416151ef6f2b9865",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294869,
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
      "evaluated_at": 1760294869
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
  "sig": "5bc24ed581bcc8d607c3e96e9cb71467372e96fd9114bba52af844ffc0aee04f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030591378
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 71585016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': 'a57eaa69ddfb92ca'}}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244890022', 'validation_error': 'Invalid routing number checksum'}}}