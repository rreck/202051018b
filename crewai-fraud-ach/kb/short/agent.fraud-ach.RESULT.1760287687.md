```json
{
  "id": "21350518b16e6336",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287687,
  "host_pid": "9e6742732c60:1",
  "hash": "45eaebfe01d05480cf07fbd4d43faf0b2d92527c07781d609a61cd944f40c710",
  "cid": "QmV145eaebfe01d05480cf07fbd4d43faf0b2d92527c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287687,
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
      "evaluated_at": 1760287687
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
  "sig": "f0348569c2ed9474ed5ea6787c0e135fb080708061bae4f9614cd78334428404"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 026009599855850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 24949986, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285763, 'matching_hash': 'c589ba109b80fe94'}}}