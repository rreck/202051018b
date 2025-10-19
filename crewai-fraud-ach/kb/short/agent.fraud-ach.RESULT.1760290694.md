```json
{
  "id": "02095b10c4cc4e0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290694,
  "host_pid": "9e6742732c60:1",
  "hash": "97d5c69488d7bd73ea18317a8773c30345f032532c0bb8c4006d4d54c6982064",
  "cid": "QmV197d5c69488d7bd73ea18317a8773c30345f03253",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290694,
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
      "evaluated_at": 1760290694
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
  "sig": "de8a7bf4205a7fc4f5b6414a470016583d93ea25d1137bfd782480c88db8cb02"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153452209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 49484202, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': 'ba46400915da6233'}}}