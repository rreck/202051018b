```json
{
  "id": "5e15a1ebc97eb538",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292928,
  "host_pid": "9e6742732c60:1",
  "hash": "1646650456f36e03e3d14867c74f65db9c0e5f6672a247ff1ca5cb28525928fa",
  "cid": "QmV11646650456f36e03e3d14867c74f65db9c0e5f66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292928,
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
      "evaluated_at": 1760292928
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
  "sig": "0ade31724c3cb8d4978f3d42e8d51ec2b0d059e070396536c20767878fe4e618"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465236749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 50306256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285764, 'matching_hash': '3442ebeb280b968f'}}}