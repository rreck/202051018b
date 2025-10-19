```json
{
  "id": "4d07c338033f8ec5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291867,
  "host_pid": "9e6742732c60:1",
  "hash": "15bc79e833c8429cafed0bd91148b76f1854e2a2306fd06b640937fee0bac036",
  "cid": "QmV115bc79e833c8429cafed0bd91148b76f1854e2a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291867,
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
      "evaluated_at": 1760291867
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
  "sig": "af1bad1893f6b746304ae51361036033e63a04a43d250c810429db7738e79466"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022959454
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 27826590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': 'd9e1e1b77e5bc9b7'}}}