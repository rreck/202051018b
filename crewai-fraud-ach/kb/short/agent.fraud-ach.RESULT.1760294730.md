```json
{
  "id": "ba65a7c9c0b37ecd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294730,
  "host_pid": "9e6742732c60:1",
  "hash": "ccfcf97140de0a5f40e01d419d992cf3f91d373196c58781dbdbeca42890bb96",
  "cid": "QmV1ccfcf97140de0a5f40e01d419d992cf3f91d3731",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294730,
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
      "evaluated_at": 1760294730
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
  "sig": "1f007af4fadc11bfa74829435851459f6bf9414ab2eca03fea4c9403ad5a3a3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248125638
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 107779977, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285764, 'matching_hash': '28ad2138639324d3'}}}