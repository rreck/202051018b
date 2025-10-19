```json
{
  "id": "4b256f878667c413",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286866,
  "host_pid": "9e6742732c60:1",
  "hash": "ca26ada454ea6aecc4e3265261d2aab63cbaf26ea61994b1dcef87a89e89d435",
  "cid": "QmV1ca26ada454ea6aecc4e3265261d2aab63cbaf26e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286866,
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
      "evaluated_at": 1760286866
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
  "sig": "ad774cf4fc343ca605a39deebd4ce7486ce8ef59f3a4d75758add01aed6a13f8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242946545
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285763, 'matching_hash': '62b45bc192f4101a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '542300570', 'validation_error': 'Invalid routing number checksum'}}}