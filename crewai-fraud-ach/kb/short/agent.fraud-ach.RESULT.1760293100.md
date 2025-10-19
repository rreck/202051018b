```json
{
  "id": "42700d18f18bb153",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293100,
  "host_pid": "9e6742732c60:1",
  "hash": "4c0ab2e738813ceab9ee8f8e85f50324c6eb7a53c34ac4e96dc058de5a720227",
  "cid": "QmV14c0ab2e738813ceab9ee8f8e85f50324c6eb7a53",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293100,
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
      "evaluated_at": 1760293100
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
  "sig": "7b643ec503bd96bd33c220cc5e61e88c28a3f36a12e7424f409e945b3b32d45f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025198728
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 19799818, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285765, 'matching_hash': 'ff4b51392b1a88ca'}}}