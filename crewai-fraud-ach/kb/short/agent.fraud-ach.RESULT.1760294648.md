```json
{
  "id": "2f6ff5ba64c2a85f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294648,
  "host_pid": "9e6742732c60:1",
  "hash": "609e25ed13189c63c3f582905720f7a3b842215738215119916f04dde4dd55f4",
  "cid": "QmV1609e25ed13189c63c3f582905720f7a3b8422157",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294648,
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
      "evaluated_at": 1760294648
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
  "sig": "4836c9671fc865d4f83d42623f87f04a626e121b75893628be82d254a0f267cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270759086
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 86805400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': 'eb79951538526d2c'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}