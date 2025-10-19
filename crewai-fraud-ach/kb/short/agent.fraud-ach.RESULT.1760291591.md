```json
{
  "id": "555a7296df8d28a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291591,
  "host_pid": "9e6742732c60:1",
  "hash": "2daa9b65dd2a6d965762b353e198bf9d91761c600e67ae4d344192648f209a43",
  "cid": "QmV12daa9b65dd2a6d965762b353e198bf9d91761c60",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291591,
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
      "evaluated_at": 1760291591
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
  "sig": "2bfc99e1a97accf5734d3d18b5e77637777ed16dbad27152a3a01b5b7158161a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 56648144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}