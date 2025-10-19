```json
{
  "id": "58d19cbef20c6be0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293824,
  "host_pid": "9e6742732c60:1",
  "hash": "aa2e6fff624227f9c292cc21ca52197d85d20231b76cb5b1e539dc89a1ea457a",
  "cid": "QmV1aa2e6fff624227f9c292cc21ca52197d85d20231",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293824,
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
      "evaluated_at": 1760293824
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
  "sig": "b86c18ad7e2cc6c5d919f91457a5dc6bc5ae224b7ffc52f177fcdc8704d80b2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021708552
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 48700288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': 'ae7eac3388a12cfd'}}}