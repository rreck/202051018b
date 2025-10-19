```json
{
  "id": "092e3f187d558861",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285890,
  "host_pid": "9e6742732c60:1",
  "hash": "2fb5a99f03e6c83a0597893a07535b24b319eaa3f586c287134b260992a4eb4b",
  "cid": "QmV12fb5a99f03e6c83a0597893a07535b24b319eaa3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285890,
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
      "evaluated_at": 1760285890
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
  "sig": "858dddd8918c6a52ca082898e99061cc2096db71a1d685b8e2d43cf2b4a700be"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000036013549
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285763, 'matching_hash': 'f1471db42dbf1c81'}}}