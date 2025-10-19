```json
{
  "id": "dc83bb0c81059081",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288622,
  "host_pid": "9e6742732c60:1",
  "hash": "e4389fa98871466def18ea809ef393bd119178159182d24c5958f58bbd9149ce",
  "cid": "QmV1e4389fa98871466def18ea809ef393bd11917815",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288622,
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
      "evaluated_at": 1760288622
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
  "sig": "c84b72d30335fa66001cdae80883b8f68200999c0545eea85ae52681157e5e72"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593598720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 20041560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': '553fe68124b88597'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}