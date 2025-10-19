```json
{
  "id": "bde3bb82a5f4d615",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293458,
  "host_pid": "9e6742732c60:1",
  "hash": "07b7468d4f8a185a1b26b2cb57d3f64a1b1bf8a5a89a102d4e6423c61406a19a",
  "cid": "QmV107b7468d4f8a185a1b26b2cb57d3f64a1b1bf8a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293458,
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
      "evaluated_at": 1760293458
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
  "sig": "bbda7ac9ee6a2b14829a83a4294295456de39cbe1279cef357b24c027d3b1ffe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596329202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 38101620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': 'fa5bd443d3b1bd8d'}}}