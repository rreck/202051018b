```json
{
  "id": "b6f47af865d5f9ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293728,
  "host_pid": "9e6742732c60:1",
  "hash": "a7ea1c0f345f7f8ae1dd7df81e4c50d00d12ac955353a2db53950605fa80c286",
  "cid": "QmV1a7ea1c0f345f7f8ae1dd7df81e4c50d00d12ac95",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293728,
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
      "evaluated_at": 1760293728
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
  "sig": "e52a7900e84cd02bf348054fc28799d41ed76219bfbe09ccf6f979d6c5c6086b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279280277
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 98946400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '5e64cdd29eaed333'}}}