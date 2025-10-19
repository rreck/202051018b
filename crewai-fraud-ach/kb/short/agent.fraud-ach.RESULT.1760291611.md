```json
{
  "id": "5b8fbf8fa17b835f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291611,
  "host_pid": "9e6742732c60:1",
  "hash": "219b30902755b3b920cf17a2aabc7d32882df98bb701c91c8fa9326befa13711",
  "cid": "QmV1219b30902755b3b920cf17a2aabc7d32882df98b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291611,
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
      "evaluated_at": 1760291611
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
  "sig": "9d01dee252ad13841ff1dcd1c583778801021f8d3af1ac45522644064bec8d65"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021861158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 45863022, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': '4f96dd6d0eca8862'}}}