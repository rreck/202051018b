```json
{
  "id": "f9a8054921466629",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290403,
  "host_pid": "9e6742732c60:1",
  "hash": "2e930a0a8ae9bab5cbaa50b3a9e45af82ef7ba566811eba00a5896392a826dc3",
  "cid": "QmV12e930a0a8ae9bab5cbaa50b3a9e45af82ef7ba56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290403,
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
      "evaluated_at": 1760290403
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
  "sig": "353cbf1a4c82e3460d70f099a3e84aa4c5fa45085cbed8829a02470baa2b1626"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039404283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 49822173, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285765, 'matching_hash': '11fbcf742e15d2b0'}}}