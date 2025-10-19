```json
{
  "id": "9210778ced901a6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294676,
  "host_pid": "9e6742732c60:1",
  "hash": "cda1f5f68da61de54542058d56044d7c74dde5d6142a2dc234cad92964720525",
  "cid": "QmV1cda1f5f68da61de54542058d56044d7c74dde5d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294676,
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
      "evaluated_at": 1760294676
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
  "sig": "64f63593b4af48639c14d38e48d1213d5c202ab9c08852951df18256e8bf243c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159904059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 108630896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285764, 'matching_hash': '7ad1725ffd2dadfd'}}}