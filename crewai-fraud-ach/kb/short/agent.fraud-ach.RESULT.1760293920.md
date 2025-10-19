```json
{
  "id": "c2337db9cef803ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293920,
  "host_pid": "9e6742732c60:1",
  "hash": "377c2c5c9a2e46ff9eb0381a2f2e7fe9b75de8991d7e159c2a8737dc8d77e307",
  "cid": "QmV1377c2c5c9a2e46ff9eb0381a2f2e7fe9b75de899",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293920,
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
      "evaluated_at": 1760293920
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
  "sig": "7c0408a49cd4960a404efc5c554b87cfcea1a44d0b2a96f765bd2d27d409786c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272056474
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 11901372, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'eb54a2a49d3a706d'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '164661952', 'validation_error': 'Invalid routing number checksum'}}}