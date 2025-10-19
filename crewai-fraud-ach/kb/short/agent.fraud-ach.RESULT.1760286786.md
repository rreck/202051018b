```json
{
  "id": "df44e51e733f2b7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286786,
  "host_pid": "9e6742732c60:1",
  "hash": "5c9723ab62f6cdb2c98670ff893e6f9276a284352df675afac5ddf0ed5cc69df",
  "cid": "QmV15c9723ab62f6cdb2c98670ff893e6f9276a28435",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286786,
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
      "evaluated_at": 1760286786
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
  "sig": "ee1c1d993bb8d1255cde51cf1dc7e0c4c827ead55a784f9ecb8189340eb3cc60"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009598219019
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285765, 'matching_hash': '253a69ee76b5426a'}}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760284979, 'matching_hash': 'f607cf2148e042a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '000042121', 'validation_error': 'Invalid routing number checksum'}}}