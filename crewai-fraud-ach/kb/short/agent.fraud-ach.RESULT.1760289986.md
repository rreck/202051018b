```json
{
  "id": "39816548a575c209",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289986,
  "host_pid": "9e6742732c60:1",
  "hash": "43c18761d74106761b02e7c4a36006058995e2a6f411d1ba9bc317f795e37cb7",
  "cid": "QmV143c18761d74106761b02e7c4a36006058995e2a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289986,
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
      "evaluated_at": 1760289986
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
  "sig": "47815f6c5a43e2c0f69c98532cd963baaac2f58b4e99e01134d424983f12071b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465632833
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 66499992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285765, 'matching_hash': '908d3acbf69a371c'}}}