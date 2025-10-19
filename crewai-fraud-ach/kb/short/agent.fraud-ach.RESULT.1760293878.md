```json
{
  "id": "843e6c21f6ecb21c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293878,
  "host_pid": "9e6742732c60:1",
  "hash": "770a40fd0c039311909bd28d5569e6d50817f44ddf5401d93cc9e5048077b1c2",
  "cid": "QmV1770a40fd0c039311909bd28d5569e6d50817f44d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293878,
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
      "evaluated_at": 1760293878
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
  "sig": "ed0ed29b613113c2139d2dfe77e7e19e0fdd9fce98aed67d4557f986f651cd17"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249286838
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 97160086, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': 'a3e7b01587d0e7c3'}}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '880809095', 'validation_error': 'Invalid routing number checksum'}}}