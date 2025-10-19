```json
{
  "id": "8d898b89a5009a67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293540,
  "host_pid": "9e6742732c60:1",
  "hash": "2066db7488bbf7b421d7c8a5ad789eabdbeecb2ddc3340097495fb42f4f799cc",
  "cid": "QmV12066db7488bbf7b421d7c8a5ad789eabdbeecb2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293540,
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
      "evaluated_at": 1760293540
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
  "sig": "4e3655265f14bfc2e5c520466503c86239a4ae1a402a1b6e16696637d8454830"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 70014560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}