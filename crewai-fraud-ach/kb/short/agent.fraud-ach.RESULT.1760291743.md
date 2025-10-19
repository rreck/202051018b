```json
{
  "id": "16abd9472c63ddc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291743,
  "host_pid": "9e6742732c60:1",
  "hash": "7e97663ac281c62216bf0a9268ce0879989ec00c9b972eb88ebd6c5443e20435",
  "cid": "QmV17e97663ac281c62216bf0a9268ce0879989ec00c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291743,
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
      "evaluated_at": 1760291743
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
  "sig": "ef0931cf0a37a2d82c921f081c7d65749afe3de5cacc03d48e3c95eb9e3cbca4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591103574
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 85135050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': 'b913753ac5280baa'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}